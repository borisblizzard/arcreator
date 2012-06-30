using System;

namespace ARCed
{
	public class ARCedException : Exception
	{
		public ARCedException(string message) : base(message) { }
	}

	public class ArcSerializationException : ARCedException
	{
		public ArcSerializationException(string message) : base(message) { }
	}
}
