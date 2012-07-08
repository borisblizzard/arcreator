
namespace RPG
{
	public class AudioFile
	{
		public string name { get; set; }
		public int volume { get; set; }
		public int pitch { get; set; }

		public AudioFile() : this("", 100, 100) { }

		public AudioFile(string name) : this(name, 100, 100) { }

		public AudioFile(string name, int volume) :
			this(name, volume, 100) { }

		public AudioFile(string name, int volume, int pitch)
		{
			this.name = name;
			this.volume = volume;
			this.pitch = pitch;
		}

		public override string ToString()
		{
			return string.Format("\"{0}\", {1}, {2}", name, volume, pitch);
		}
	}
}
