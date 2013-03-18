float4x4 WorldViewProjection : WORLDVIEWPROJ;

struct VS_INPUT
{
	float4 position : POSITION;
	float4 color : COLOR0;
};

struct VS_OUTPUT
{
	float4 position : POSITION;
	float4 color : COLOR0;
};

VS_OUTPUT main(VS_INPUT vertex)
{
	VS_OUTPUT v;
	v.position = mul(vertex.position, WorldViewProjection);
	v.color = vertex.color;
	return v;
}