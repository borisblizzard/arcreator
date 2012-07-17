
namespace RPG
{
    /// <summary>
    /// Data class for audio files. Common to all formats (BGM, BGS, ME, SE). 
    /// </summary>
	public class AudioFile
	{
        /// <summary>
        /// The sound file name.
        /// </summary>
		public string name { get; set; }
        /// <summary>
        /// The sound's volume (0..100). 
        /// The default values are 100 for BGM and ME and 80 for BGS and SE.
        /// </summary>
		public int volume { get; set; }
        /// <summary>
        /// The sound's pitch (50..150). 
        /// The default value is 100.
        /// </summary>
		public int pitch { get; set; }

        /// <summary>
        /// Creates a new instance of an RPG.AudioFile.
        /// </summary>
        /// <param name="name">Name of the sound file.</param>
        /// <param name="volume">The sound's volume.</param>
        /// <param name="pitch">The sound's pitch.</param>
		public AudioFile(string name = "", int volume = 100, int pitch = 100)
		{
			this.name = name;
			this.volume = volume;
			this.pitch = pitch;
		}

        /// <summary>
        /// Returns a <see langword="string"/> that represents the current object.
        /// </summary>
        /// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("\"{0}\", {1}, {2}", name, volume, pitch);
		}
	}
}
