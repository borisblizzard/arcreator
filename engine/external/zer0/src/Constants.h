#ifndef ZER0_CONSTANTS_H
#define ZER0_CONSTANTS_H

// numeric system constants
#define TEXTURE_UNLOAD_TIME (5.0f)
#define E_TOLERANCE (0.01f)

#define CFG_TITLE "Title"
#define CFG_RESOLUTION "Resolution"
#define CFG_FULLSCREEN "Fullscreen"
#define CFG_FRAME_RATE "FrameRate"
#define CFG_INACTIVE_AUDIO "InactiveAudio"
#define CFG_FONT_BASE_SIZE "FontBaseSize"
#define CFG_GAME_VERSION "GameVersion"

#define ARC_PIXEL_SHADER "\
float4 alpha : COLOR0; \
float4 color : COLOR1; \
float4 tone : COLOR2; \
sampler2D tex0; \
float3 rgb2hsl = {0.299, 0.587, 0.114}; \
float4 main(float2 texcoord0 : TEXCOORD0) : COLOR0 \
{ \
	float4 c = tex2D(tex0, texcoord0); \
	if (c.a > 0) \
	{ \
		c.a = c.a * alpha.a; \
		if (c.a > 0) \
		{ \
			if (color.a > 0) \
			{ \
				c.rgb = c.rgb * (1.0 - color.a) + color.rgb * color.a; \
			} \
			if (tone.a == 1) \
			{ \
				c.rgb = c.rgb + (tone.rgb - 0.5) * 2; \
			} \
			else \
			{ \
				float gray = dot(c.rgb, rgb2hsl); \
				c.rgb = (c.rgb - gray) * tone.a + gray + (tone.rgb - 0.5) * 2; \
			} \
		} \
	} \
	return c; \
} \
"

#define ARC_VERTEX_SHADER "\
float4x4 WorldViewProjection : WORLDVIEWPROJ; \
struct VS_INPUT { \
	float4 position : POSITION; \
	float4 color : COLOR0; \
}; \
struct VS_OUTPUT { \
	float4 position : POSITION; \
	float4 color : COLOR0; \
}; \
VS_OUTPUT main(VS_INPUT vertex) \
{ \
	VS_OUTPUT v; \
	v.position = mul(vertex.position, WorldViewProjection); \
	v.color = vertex.color; \
	return v; \
} \
"

#endif
