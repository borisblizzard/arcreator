using SysColor = System.Drawing.Color;

// TODO: Clamp values

namespace RPG
{
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

        public static implicit operator SysColor(Color color)
        {
            return SysColor.FromArgb((int)color.alpha, (int)color.red,
                (int)color.green, (int)color.blue);
        }

        public static implicit operator Color(SysColor color)
        {
            return new Color(color.R, color.G, color.B, color.A);
        }
    }
}
