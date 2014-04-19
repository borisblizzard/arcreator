float4 alpha : COLOR0;
float4 color : COLOR1;
float4 tone : COLOR2;
sampler2D tex0;
float3 rgb2hsl = {0.299, 0.587, 0.114};

float4 main(float2 texcoord0 : TEXCOORD0) : COLOR0
{
	float4 c = tex2D(tex0, texcoord0);
	if (c.a > 0)
	{
		c.a = c.a * alpha.a;
		if (c.a > 0)
		{
			if (color.a > 0)
			{
				c.rgb = c.rgb * (1.0 - color.a) + color.rgb * color.a;
			}
			if (tone.a == 1)
			{
				c.rgb = c.rgb + (tone.rgb - 0.5) * 2;
			}
			else
			{
				float gray = dot(c.rgb, rgb2hsl);
				c.rgb = (c.rgb - gray) * tone.a + gray + (tone.rgb - 0.5) * 2;
			}
		}
	}
	return c;
}
