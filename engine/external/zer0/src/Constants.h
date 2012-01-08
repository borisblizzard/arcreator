#ifndef ZER0_CONSTANTS_H
#define ZER0_CONSTANTS_H

// numeric system constants
#define TEXTURE_UNLOAD_TIME (5.0f)
#define E_TOLERANCE (0.01f)

#define CFG_TITLE "Title"
#define CFG_RESOLUTION "Resolution"
#define CFG_FULLSCREEN "Fullscreen"
#define CFG_FRAME_RATE "FrameRate"

#define ARC_PIXEL_SHADER "\
struct PS_INPUT \
{ \
	float2 tex0 : TEXCOORD0; \
	float4 color : COLOR0; \
	float4 tone : COLOR1; \
}; \
sampler2D tex0; \
float3 rgb2hsl = {0.299, 0.587, 0.114}; \
float4 main(PS_INPUT data) : COLOR0 \
{ \
	float4 c = tex2D(tex0, data.tex0); \
	if (c.a > 0) \
	{ \
		if (data.color.a > 0) \
		{ \
			c.rgb = c.rgb * (1.0 - data.color.a) + data.color.rgb * data.color.a; \
		} \
		if (data.tone.a == 1) \
		{ \
			c.rgb = c.rgb + (data.tone.rgb - 0.5) * 2; \
		} \
		else \
		{ \
			float gray = c.r * 0.299 + c.g * 0.587 + c.b * 0.114; \
			c.rgb = (c.rgb - gray) * data.tone.a + gray + (data.tone.rgb - 0.5) * 2; \
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
