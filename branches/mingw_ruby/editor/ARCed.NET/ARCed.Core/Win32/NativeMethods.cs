#region Using Directives

using System;
using System.Diagnostics.CodeAnalysis;
using System.Drawing;
using System.Runtime.InteropServices;
using System.Text;

#endregion

namespace ARCed.Core.Win32
{
    /// <summary>
    /// Static class containing methods that utilize P/Invoke or other unmanaged libraries
    /// </summary>
    public static class NativeMethods
    {
		/// <summary>
		/// Constant flag used for suspending and resuming drawing of controls.
		/// </summary>
		public const int WM_SETREDRAW = 0x0B;

		/// <summary>
		/// Delegate representing the hook procedure method.
		/// </summary>
		/// <param name="code">The type of hook procedure to be installed</param>
		/// <param name="wParam">Additional message-specific information.</param>
		/// <param name="lParam">Additional message-specific information.</param>
		/// <returns>Value specifying the result of the hook processing</returns>
		public delegate IntPtr HookProc(int code, IntPtr wParam, IntPtr lParam);

		/// <summary>
		/// Captures the mouse and tracks its movement until the user releases the left button, presses the ESC key, 
		/// or moves the mouse outside the drag rectangle around the specified point.
		/// </summary>
		/// <param name="hWnd">A handle to the window receiving mouse input.</param>
		/// <param name="pt">Initial position of the mouse, in screen coordinates.</param>
		/// <returns>If the user moved the mouse outside of the drag rectangle while holding down the left button, 
		/// the return value is nonzero, else 0.</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
        [return: MarshalAs(UnmanagedType.Bool)]
		public static extern bool DragDetect(IntPtr hWnd, Point pt);

		/// <summary>
		/// Retrieves the handle to the window that has the keyboard focus.
		/// </summary>
		/// <returns>Handle to the window with the keyboard focus.</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
        public static extern IntPtr GetFocus();

		/// <summary>
		/// Sets the keyboard focus to the specified window.
		/// </summary>
		/// <param name="hWnd">A handle to the window that will receive the keyboard input.</param>
		/// <returns>If the function succeeds, the return value is the handle to the window that previously had the keyboard focus.</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
        public static extern IntPtr SetFocus(IntPtr hWnd);

		/// <summary>
		/// Places (posts) a message in the message queue associated with the thread that created the specified 
		/// window and returns without waiting for the thread to process the message.
		/// </summary>
		/// <param name="hWnd">A handle to the window whose window procedure is to receive the message.</param>
		/// <param name="msg">The message to be posted.</param>
		/// <param name="wParam">Additional message-specific information.</param>
		/// <param name="lParam">Additional message-specific information.</param>
		/// <returns>If the function succeeds, the return value is nonzero, else 0.</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
        [return: MarshalAs(UnmanagedType.Bool)]
        public static extern bool PostMessage(IntPtr hWnd, int msg, uint wParam, uint lParam);

		/// <summary>
		/// Sends the specified message to a window or windows.
		/// </summary>
		/// <param name="hWnd">Handle to the window whose window procedure will receive the message</param>
		/// <param name="wMsg">Message to be sent</param>
		/// <param name="wParam">Additional message-specific information</param>
		/// <param name="lParam">Additional message-specific information</param>
		/// <returns>The return value specifies the result of the message processing; it depends on the message sent</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
        public static extern uint SendMessage(IntPtr hWnd, int wMsg, uint wParam, uint lParam);

		/// <summary>
		/// Sends the specified message to a window or windows.
		/// </summary>
		/// <param name="hWnd">Handle to the window whose window procedure will receive the message</param>
		/// <param name="wMsg">Message to be sent</param>
		/// <param name="wParam">Additional message-specific information</param>
		/// <param name="lParam">Additional message-specific information</param>
		/// <returns>The return value specifies the result of the message processing; it depends on the message sent</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
		public static extern int SendMessage(IntPtr hWnd, Int32 wMsg, bool wParam, Int32 lParam);

		/// <summary>
		/// Sets the specified window's show state.
		/// </summary>
		/// <param name="hWnd">A handle to the window.</param>
		/// <param name="cmdShow">Controls how the window is to be shown.</param>
		/// <returns>If the window was previously visible, the return value is nonzero, else 0.</returns>
        [DllImport("User32.dll", CharSet = CharSet.Unicode)]
        public static extern int ShowWindow(IntPtr hWnd, short cmdShow);

		/// <summary>
		/// Changes the size, position, and Z order of a child, pop-up, or top-level window.
		/// </summary>
		/// <param name="hWnd">Handle to the window.</param>
		/// <param name="hWndAfter">A handle to the window to precede the positioned window in the Z order.</param>
		/// <param name="x">The new position of the left side of the window, in client coordinates.</param>
		/// <param name="y">The new position of the top of the window, in client coordinates.</param>
		/// <param name="width">The new width of the window, in pixels.</param>
		/// <param name="height">The new height of the window, in pixels.</param>
		/// <param name="flags">The window sizing and positioning flags.</param>
		/// <returns>If the function succeeds, the return value is nonzero.</returns>
        [DllImport("User32.dll", CharSet = CharSet.Unicode)]
        public static extern int SetWindowPos(IntPtr hWnd, IntPtr hWndAfter, int x, int y, int width, int height, FlagsSetWindowPos flags);

		/// <summary>
		/// Retrieves information about the specified window.
		/// </summary>
		/// <param name="hWnd">A handle to the window and, indirectly, the class to which the window belongs.</param>
		/// <param name="index">The zero-based offset to the value to be get.</param>
		/// <returns>If the function succeeds, the return value is the requested value, else 0.</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
		public static extern int GetWindowLong(IntPtr hWnd, int index);

		/// <summary>
		/// Changes an attribute of the specified window.
		/// </summary>
		/// <param name="hWnd">A handle to the window and, indirectly, the class to which the window belongs.</param>
		/// <param name="index">The zero-based offset to the value to be set.</param>
		/// <param name="value">The replacement value.</param>
		/// <returns>If the function succeeds, the return value is the previous value of the specified 32-bit integer, else 0.</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
		public static extern int SetWindowLong(IntPtr hWnd, int index, int value);

		/// <summary>
		/// Shows or hides the specified scroll bar.
		/// </summary>
		/// <param name="hWnd">Handle to a scroll bar control or a window with a standard scroll bar.</param>
		/// <param name="wBar">Specifies the scroll bar(s) to be shown or hidden.</param>
		/// <param name="bShow">Specifies whether the scroll bar is shown or hidden</param>
		/// <returns>If the function succeeds, the return value is nonzero.</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
		public static extern int ShowScrollBar(IntPtr hWnd, int wBar, int bShow);

		/// <summary>
		/// Retrieves a handle to the window that contains the specified point.
		/// </summary>
		/// <param name="point">The point to be checked.</param>
		/// <returns>Handle to the window that contains the point, or null if none found.</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
        [SuppressMessage("Microsoft.Portability", "CA1901:PInvokeDeclarationsShouldBePortable", MessageId = "0")]
		public static extern IntPtr WindowFromPoint(Point point);

		/// <summary>
		/// Retrieves the thread identifier of the calling thread.
		/// </summary>
		/// <returns>Thread identifier of the calling thread.</returns>
        [DllImport("Kernel32.dll", CharSet = CharSet.Unicode)]
        public static extern int GetCurrentThreadId();

		/// <summary>
		/// Installs an application-defined hook procedure into a hook chain.
		/// </summary>
		/// <param name="code">The type of hook procedure to be installed.</param>
		/// <param name="func">A pointer to the hook procedure.</param>
		/// <param name="hInstance">A handle to the DLL containing the hook procedure pointed to by the <see cref="func"/> parameter.</param>
		/// <param name="threadID">The identifier of the thread with which the hook procedure is to be associated.</param>
		/// <returns>If the function succeeds, the return value is the handle to the hook procedure.</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
        public static extern IntPtr SetWindowsHookEx(HookType code, HookProc func, IntPtr hInstance, int threadID);

		/// <summary>
		/// Removes a hook procedure installed in a hook chain by the <see cref="SetWindowsHookEx"/> function.
		/// </summary>
		/// <param name="hhook">Handle to the hook to be removed.</param>
		/// <returns>If the function succeeds, the return value is nonzero.</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
        public static extern int UnhookWindowsHookEx(IntPtr hhook);

		/// <summary>
		/// Passes the hook information to the next hook procedure in the current hook chain
		/// </summary>
		/// <param name="hhook">This parameter is ignored</param>
		/// <param name="code">The hook code passed to the current hook procedure</param>
		/// <param name="wParam">Value passed to the current hook procedure. 
		/// The meaning of this parameter depends on the type of hook associated with the current hook chain</param>
		/// <param name="lParam">Value passed to the current hook procedure. 
		/// The meaning of this parameter depends on the type of hook associated with the current hook chain</param>
		/// <returns>Value is returned by the next hook procedure in the chain</returns>
		[DllImport("User32.dll", CharSet = CharSet.Unicode)]
        public static extern IntPtr CallNextHookEx(IntPtr hhook, int code, IntPtr wParam, IntPtr lParam);

		/// <summary>
		/// Adds a font resource from a memory image to the system.
		/// </summary>
		/// <param name="pbFont">A pointer to a font resource</param>
		/// <param name="cbFont">The number of bytes in the font resource that is pointed to by pbFont</param>
		/// <param name="pdv">Reserved. Must be 0</param>
		/// <param name="pcFonts">A pointer to a variable that specifies the number of fonts installed</param>
		/// <returns>If the function succeeds, the return value specifies the number of fonts added, else 0</returns>
		[DllImport("Gdi32.dll", CharSet = CharSet.Unicode)]
        public static extern IntPtr AddFontMemResourceEx(IntPtr pbFont, uint cbFont, IntPtr pdv,
            [In] ref uint pcFonts);

		/// <summary>
		/// Adds a font resource into the system. The font will be marked private non enumerable.
		/// </summary>
		/// <param name="lpszFilename">Filename of the font resource file</param>
		/// <param name="fl">The characteristics of the font to be added to the system</param>
		/// <param name="pdv">Reserved. Must be zero.</param>
		/// <returns>If the function succeeds, the return value specifies the number of fonts added, else 0</returns>
		[DllImport("Gdi32.dll", CharSet = CharSet.Unicode)]
        public static extern int AddFontResourceEx(string lpszFilename, uint fl, IntPtr pdv);

        /// <summary>
        /// Writes a configuration value to an .ini file
        /// </summary>
        /// <param name="section">The section name</param>
        /// <param name="key">The key name</param>
        /// <param name="val">The value to write</param>
        /// <param name="filePath">The path to the file</param>
        /// <returns>Error code</returns>
		[DllImport("Kernel32.dll", CharSet = CharSet.Unicode)]
        public static extern long WritePrivateProfileString(string section,
            string key, string val, string filePath);

        /// <summary>
        /// Reads a configuration value to an .ini file
        /// </summary>
        /// <param name="section">The section name</param>
        /// <param name="key">The key name</param>
        /// <param name="def">Default string if value cannot be found</param>
        /// <param name="retVal">The buffer to write the value to</param>
        /// <param name="size">The maximum buffer size</param>
        /// <param name="filePath">The path to the file</param>
        /// <returns>Error code</returns>
        [DllImport("Kernel32.dll", CharSet = CharSet.Unicode)]
        public static extern int GetPrivateProfileString(string section,
                 string key, string def, StringBuilder retVal, int size, string filePath);

        /// <summary>
        /// Creates a cursor object and returns it
        /// </summary>
        /// <param name="str">The name of the resource file</param>
        /// <returns>A handle to a cursor object</returns>
        [DllImport("User32.dll", CharSet = CharSet.Unicode)]
        public static extern IntPtr LoadCursorFromFile(String str);

        /// <summary>
        /// Sets the foreground window
        /// </summary>
        /// <param name="hWnd">A handle to a window</param>
        /// <returns>Flag if error occurred</returns>
        [DllImport("User32.dll", CharSet = CharSet.Unicode)]
        public static extern bool SetForegroundWindow(IntPtr hWnd);

        /// <summary>
        /// Changes the icon of an attached console
        /// </summary>
        /// <param name="hIcon">A handle to an icon</param>
        /// <returns>Flag if error occurred</returns>
		[DllImport("Kernel32.dll", CharSet = CharSet.Unicode)]
        public static extern bool SetConsoleIcon(IntPtr hIcon);

        /// <summary>
        /// Obtains the short path form of a specified input path
        /// </summary>
        /// <param name="lpszLongPath">Points to a null-terminated path string. The function 
        /// obtains the short form of this path</param>
        /// <param name="lpszShortPath">Points to a buffer to receive the null-terminated 
        /// short form of the path specified by lpszLongPath</param>
        /// <param name="cchBuffer">The size of the buffer that lpszShortPath points to</param>
        /// <returns>Value is the length, in characters, of the string copied to lpszShortPath</returns>
		[DllImport("Kernel32.dll", CharSet = CharSet.Unicode)]
        public static extern uint GetShortPathName(string lpszLongPath,
            [Out] StringBuilder lpszShortPath, uint cchBuffer);

        /// <summary>
        /// Allocates a new console for the calling process
        /// </summary>
        /// <returns>Non-zero if successful, zero otherwise</returns>
		[DllImport("Kernel32.dll", EntryPoint = "AllocConsole", CharSet = CharSet.Unicode)]
        public static extern int AllocConsole();
	}
}