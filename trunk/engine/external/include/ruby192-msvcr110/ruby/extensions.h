#ifndef RUBY_EXTENSIONS_H
#define RUBY_EXTENSIONS_H

extern "C"
{
	void Init_win32api();
	void Init_socket();
	void Init_zlib();

}

#endif
