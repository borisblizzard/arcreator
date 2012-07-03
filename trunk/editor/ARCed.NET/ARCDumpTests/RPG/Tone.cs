
// TODO: Clamp values

class Tone
{
	public float red { get; set; }
	public float green { get; set; }
	public float blue { get; set; }
	public float gray { get; set; }

	public Tone() : this(0, 0, 0, 0) { }

	public Tone(float red, float green, float blue) :
		this(red, green, blue, 255) { }

	public Tone(float red, float green, float blue, float gray)
	{
		this.red = red;
		this.green = green;
		this.blue = blue;
		this.gray = gray;
	}

	public void set(float red, float green, float blue)
	{
		set(red, green, blue, this.gray);
	}

	public void set(float red, float green, float blue, float gray)
	{
		this.red = red;
		this.green = green;
		this.blue = blue;
		this.gray = gray;
	}
}
