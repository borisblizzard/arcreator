#region License

/* Copyright (c) 2006 Leslie Sanford
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy 
 * of this software and associated documentation files (the "Software"), to 
 * deal in the Software without restriction, including without limitation the 
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
 * sell copies of the Software, and to permit persons to whom the Software is 
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in 
 * all copies or substantial portions of the Software. 
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
 * THE SOFTWARE.
 */

#endregion

#region Using Directives

using System;
using System.ComponentModel;
using System.Diagnostics;
using System.Runtime.InteropServices;

#endregion

namespace ARCed.Controls
{

	/// <summary>
	/// Defines constants representing the timing format used by the Time struct.
	/// </summary>
	public enum TimeType
	{
		Milliseconds = 0x0001,
		Samples = 0x0002,
		Bytes = 0x0004,
		Smpte = 0x0008,
		Midi = 0x0010,
		Ticks = 0x0020
	}

	/// <summary>
	/// Represents the Windows Multimedia MMTIME structure.
	/// </summary>
	[StructLayout(LayoutKind.Explicit)]
	public struct Time
	{
		[FieldOffset(0)]
		public int type;

		[FieldOffset(4)]
		public int milliseconds;

		[FieldOffset(4)]
		public int samples;

		[FieldOffset(4)]
		public int byteCount;

		[FieldOffset(4)]
		public int ticks;

		//
		// SMPTE
		//

		[FieldOffset(4)]
		public byte hours;

		[FieldOffset(5)]
		public byte minutes;

		[FieldOffset(6)]
		public byte seconds;

		[FieldOffset(7)]
		public byte frames;

		[FieldOffset(8)]
		public byte framesPerSecond;

		[FieldOffset(9)]
		public byte dummy;

		[FieldOffset(10)]
		public byte pad1;

		[FieldOffset(11)]
		public byte pad2;

		//
		// MIDI
		//

		[FieldOffset(4)]
		public int songPositionPointer;
	}

	/// <summary>
	/// Defines constants for the multimedia Timer's event types.
	/// </summary>
	public enum TimerMode
	{
		/// <summary>
		/// Timer event occurs once.
		/// </summary>
		OneShot,

		/// <summary>
		/// Timer event occurs periodically.
		/// </summary>
		Periodic
	};

	/// <summary>
	/// Represents information about the multimedia Timer's capabilities.
	/// </summary>
	[StructLayout(LayoutKind.Sequential)]
	public struct TimerCaps
	{
		/// <summary>
		/// Minimum supported period in milliseconds.
		/// </summary>
		public int periodMin;

		/// <summary>
		/// Maximum supported period in milliseconds.
		/// </summary>
		public int periodMax;
	}

	/// <summary>
	/// Represents the Windows multimedia timer.
	/// </summary>
	public sealed class HighPrecisionTimer : IComponent
	{
		#region Timer Members

		#region Delegates

		// Represents the method that is called by Windows when a timer event occurs.
		private delegate void TimeProc(int id, int msg, int user, int param1, int param2);

		// Represents methods that raise events.
		private delegate void EventRaiser(EventArgs e);

		#endregion

		#region Win32 Multimedia Timer Functions

		// Gets timer capabilities.
		[DllImport("winmm.dll")]
		private static extern int timeGetDevCaps(ref TimerCaps caps,
			int sizeOfTimerCaps);

		// Creates and starts the timer.
		[DllImport("winmm.dll")]
		private static extern int timeSetEvent(int delay, int resolution,
			TimeProc proc, int user, int mode);

		// Stops and destroys the timer.
		[DllImport("winmm.dll")]
		private static extern int timeKillEvent(int id);

		// Indicates that the operation was successful.
		private const int TIMERR_NOERROR = 0;

		#endregion

		#region Fields

		// Timer identifier.
		private int timerID;

		// Timer mode.
		private volatile TimerMode mode;

		// Period between timer events in milliseconds.
		private volatile int period;

		// Timer resolution in milliseconds.
		private volatile int resolution;

		// Called by Windows when a timer periodic event occurs.
		private TimeProc timeProcPeriodic;

		// Called by Windows when a timer one shot event occurs.
		private TimeProc timeProcOneShot;

		// Represents the method that raises the Tick event.
		private EventRaiser tickRaiser;

		// Indicates whether or not the timer is running.
	    private bool running;

		// Indicates whether or not the timer has been disposed.
	    private volatile bool disposed;

		// The ISynchronizeInvoke object to use for marshaling events.
	    private ISynchronizeInvoke synchronizingObject;

		// For implementing IComponent.
	    private ISite site;

		// Multimedia timer capabilities.
		private static readonly TimerCaps caps;

		#endregion

		#region Events

		/// <summary>
		/// Occurs when the Timer has started;
		/// </summary>
		public event EventHandler Started;

		/// <summary>
		/// Occurs when the Timer has stopped;
		/// </summary>
		public event EventHandler Stopped;

		/// <summary>
		/// Occurs when the time period has elapsed.
		/// </summary>
		public event EventHandler Tick;

		#endregion

		#region Construction

		/// <summary>
		/// Initialize class.
		/// </summary>
		static HighPrecisionTimer()
		{
			// Get multimedia timer capabilities.
			timeGetDevCaps(ref caps, Marshal.SizeOf(caps));
		}

		/// <summary>
		/// Initializes a new instance of the Timer class with the specified IContainer.
		/// </summary>
		/// <param name="container">
		/// The IContainer to which the Timer will add itself.
		/// </param>
		public HighPrecisionTimer(IContainer container)
		{
			container.Add(this);
			Initialize();
		}

		/// <summary>
		/// Initializes a new instance of the Timer class.
		/// </summary>
		public HighPrecisionTimer()
		{
			Initialize();
		}

		~HighPrecisionTimer()
		{
			if (IsRunning)
			{
				// Stop and destroy timer.
				timeKillEvent(timerID);
			}
		}

		// Initialize timer with default values.
		private void Initialize()
		{
			this.mode = TimerMode.Periodic;
			this.period = Capabilities.periodMin;
			this.resolution = 1;

			running = false;

			timeProcPeriodic = this.TimerPeriodicEventCallback;
			timeProcOneShot = this.TimerOneShotEventCallback;
			tickRaiser = this.OnTick;
		}

		#endregion

		#region Methods

		/// <summary>
		/// Starts the timer.
		/// </summary>
		/// <exception cref="ObjectDisposedException">
		/// The timer has already been disposed.
		/// </exception>
		/// <exception cref="TimerStartException">
		/// The timer failed to start.
		/// </exception>
		public void Start()
		{
			#region Require

			if (disposed)
			{
				throw new ObjectDisposedException("Timer");
			}

			#endregion

			#region Guard

			if (IsRunning)
			{
				return;
			}

			#endregion

			// If the periodic event callback should be used.
			if (Mode == TimerMode.Periodic)
			{
				// Create and start timer.
				timerID = timeSetEvent(Period, Resolution, timeProcPeriodic, 0, (int)Mode);
			}
			// Else the one shot event callback should be used.
			else
			{
				// Create and start timer.
				timerID = timeSetEvent(Period, Resolution, timeProcOneShot, 0, (int)Mode);
			}

			// If the timer was created successfully.
			if (timerID != 0)
			{
				running = true;

				if (SynchronizingObject != null && SynchronizingObject.InvokeRequired)
				{
					SynchronizingObject.BeginInvoke(
						new EventRaiser(OnStarted),
						new object[] { EventArgs.Empty });
				}
				else
				{
					OnStarted(EventArgs.Empty);
				}
			}
			else
			{
				throw new TimerStartException("Unable to start multimedia Timer.");
			}
		}

		/// <summary>
		/// Stops timer.
		/// </summary>
		/// <exception cref="ObjectDisposedException">
		/// If the timer has already been disposed.
		/// </exception>
		public void Stop()
		{
			#region Require

			if (disposed)
			{
				throw new ObjectDisposedException("Timer");
			}

			#endregion

			#region Guard

			if (!running)
			{
				return;
			}

			#endregion

			// Stop and destroy timer.
			int result = timeKillEvent(timerID);

			Debug.Assert(result == TIMERR_NOERROR);

			running = false;

			if (SynchronizingObject != null && SynchronizingObject.InvokeRequired)
			{
				SynchronizingObject.BeginInvoke(
					new EventRaiser(OnStopped),
					new object[] { EventArgs.Empty });
			}
			else
			{
				OnStopped(EventArgs.Empty);
			}
		}

		#region Callbacks

		// Callback method called by the Win32 multimedia timer when a timer
		// periodic event occurs.
		private void TimerPeriodicEventCallback(int id, int msg, int user, int param1, int param2)
		{
			if (synchronizingObject != null)
			{
				synchronizingObject.BeginInvoke(tickRaiser, new object[] { EventArgs.Empty });
			}
			else
			{
				OnTick(EventArgs.Empty);
			}
		}

		// Callback method called by the Win32 multimedia timer when a timer
		// one shot event occurs.
		private void TimerOneShotEventCallback(int id, int msg, int user, int param1, int param2)
		{
			if (synchronizingObject != null)
			{
				synchronizingObject.BeginInvoke(tickRaiser, new object[] { EventArgs.Empty });
				Stop();
			}
			else
			{
				OnTick(EventArgs.Empty);
				Stop();
			}
		}

		#endregion

		#region Event Raiser Methods

		// Raises the Disposed event.
		private void OnDisposed(EventArgs e)
		{
			EventHandler handler = Disposed;

			if (handler != null)
			{
				handler(this, e);
			}
		}

		// Raises the Started event.
		private void OnStarted(EventArgs e)
		{
			EventHandler handler = Started;

			if (handler != null)
			{
				handler(this, e);
			}
		}

		// Raises the Stopped event.
		private void OnStopped(EventArgs e)
		{
			EventHandler handler = Stopped;

			if (handler != null)
			{
				handler(this, e);
			}
		}

		// Raises the Tick event.
		private void OnTick(EventArgs e)
		{
			EventHandler handler = Tick;

			if (handler != null)
			{
				handler(this, e);
			}
		}

		#endregion

		#endregion

		#region Properties

		/// <summary>
		/// Gets or sets the object used to marshal event-handler calls.
		/// </summary>
		public ISynchronizeInvoke SynchronizingObject
		{
			get
			{
				#region Require

				if (disposed)
				{
					throw new ObjectDisposedException("Timer");
				}

				#endregion

				return synchronizingObject;
			}
			set
			{
				#region Require

				if (disposed)
				{
					throw new ObjectDisposedException("Timer");
				}

				#endregion

				synchronizingObject = value;
			}
		}

		/// <summary>
		/// Gets or sets the time between Tick events.
		/// </summary>
		/// <exception cref="ObjectDisposedException">
		/// If the timer has already been disposed.
		/// </exception>   
		public int Period
		{
			get
			{
				#region Require

				if (disposed)
				{
					throw new ObjectDisposedException("Timer");
				}

				#endregion

				return period;
			}
			set
			{
				#region Require

				if (disposed)
				{
					throw new ObjectDisposedException("Timer");
				}
				else if (value < Capabilities.periodMin || value > Capabilities.periodMax)
				{
					throw new ArgumentOutOfRangeException("Period", value,
						"Multimedia Timer period out of range.");
				}

				#endregion

				period = value;

				if (IsRunning)
				{
					Stop();
					Start();
				}
			}
		}

		/// <summary>
		/// Gets or sets the timer resolution.
		/// </summary>
		/// <exception cref="ObjectDisposedException">
		/// If the timer has already been disposed.
		/// </exception>        
		/// <remarks>
		/// The resolution is in milliseconds. The resolution increases 
		/// with smaller values; a resolution of 0 indicates periodic events 
		/// should occur with the greatest possible accuracy. To reduce system 
		/// overhead, however, you should use the maximum value appropriate 
		/// for your application.
		/// </remarks>
		public int Resolution
		{
			get
			{
				#region Require

				if (disposed)
				{
					throw new ObjectDisposedException("Timer");
				}

				#endregion

				return resolution;
			}
			set
			{
				#region Require

				if (disposed)
				{
					throw new ObjectDisposedException("Timer");
				}
				else if (value < 0)
				{
					throw new ArgumentOutOfRangeException("Resolution", value,
						"Multimedia timer resolution out of range.");
				}

				#endregion

				resolution = value;

				if (IsRunning)
				{
					Stop();
					Start();
				}
			}
		}

		/// <summary>
		/// Gets the timer mode.
		/// </summary>
		/// <exception cref="ObjectDisposedException">
		/// If the timer has already been disposed.
		/// </exception>
		public TimerMode Mode
		{
			get
			{
				#region Require

				if (disposed)
				{
					throw new ObjectDisposedException("Timer");
				}

				#endregion

				return mode;
			}
			set
			{
				#region Require

				if (disposed)
				{
					throw new ObjectDisposedException("Timer");
				}

				#endregion

				mode = value;

				if (IsRunning)
				{
					Stop();
					Start();
				}
			}
		}

		/// <summary>
		/// Gets a value indicating whether the Timer is running.
		/// </summary>
		public bool IsRunning
		{
			get
			{
				return running;
			}
		}

		/// <summary>
		/// Gets the timer capabilities.
		/// </summary>
		public static TimerCaps Capabilities
		{
			get
			{
				return caps;
			}
		}

		#endregion

		#endregion

		#region IComponent Members

		public event EventHandler Disposed;

		public ISite Site
		{
			get
			{
				return site;
			}
			set
			{
				site = value;
			}
		}

		#endregion

		#region IDisposable Members

		/// <summary>
		/// Frees timer resources.
		/// </summary>
		public void Dispose()
		{
			#region Guard

			if (disposed)
			{
				return;
			}

			#endregion

			if (IsRunning)
			{
				Stop();
			}

			disposed = true;

			OnDisposed(EventArgs.Empty);
		}

		#endregion
	}

	/// <summary>
	/// The exception that is thrown when a timer fails to start.
	/// </summary>
	public class TimerStartException : ApplicationException
	{
		/// <summary>
		/// Initializes a new instance of the TimerStartException class.
		/// </summary>
		/// <param name="message">
		/// The error message that explains the reason for the exception. 
		/// </param>
		public TimerStartException(string message)
			: base(message)
		{
		}
	}
}
