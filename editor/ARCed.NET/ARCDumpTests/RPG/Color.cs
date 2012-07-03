
// TODO: Clamp values

public class Color
{
	public float red { get; set; }
	public float green { get; set; }
	public float blue { get; set; }
	public float alpha { get; set; }

	public Color() : this(0.0f, 0.0f, 0.0f, 0.0f) { }

	public Color(float red, float green, float blue) :
		this(red, green, blue, 255.0f) { }

	public Color(float red, float green, float blue, float alpha)
	{
		this.red = red;
		this.green = green;
		this.blue = blue;
		this.alpha = alpha;
	}

	public void set(float red, float green, float blue)
	{
		set(red, green, blue, this.alpha);
	}

	public void set(float red, float green, float blue, float alpha)
	{
		this.red = red;
		this.green = green;
		this.blue = blue;
		this.alpha = alpha;
	}
}
