#region Using Directives

using System;

#endregion

namespace ARCed
{
    /// <summary>
    /// Generic exception used for ARCed related errors.
    /// </summary>
	public class ARCedException : Exception
	{
        /// <summary>
        /// Default constructor
        /// </summary>
        /// <param name="message">Exception message</param>
		public ARCedException(string message) : base(message) { }
	}

    /// <summary>
    /// Generic exception used for ARCed serialization errors. 
    /// </summary>
	public class ArcSerializationException : ARCedException
	{
        /// <summary>
        /// Default constructor
        /// </summary>
        /// <param name="message">Exception message</param>
		public ArcSerializationException(string message) : base(message) { }
	}
}
