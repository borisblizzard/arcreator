
namespace ARCed
{
    /// <summary>
    /// Static class containing flags indicating ARCed environment flags.
    /// </summary>
    public static class Runtime
    {
        // TODO: Convert this class to an enum

        /// <summary>
        /// Flag indicating if ARCed.NET is being ran with Debug flag.
        /// </summary>
        public static bool Debug { get; set; }

        /// <summary>
        /// Flag indicating if ARCed.NET is being ran with Portable flag.
        /// </summary>
        public static bool Portable { get; set; }

        /// <summary>
        /// Flag indicating if ARCed.NET is being ran with Legacy flag.
        /// </summary>
        public static bool Legacy { get; set; }

        /// <summary>
        /// Flag indicating if ARCed.NET is being ran with Logging flag.
        /// </summary>
        public static bool Logging { get; set; }
    }
}
