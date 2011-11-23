/// @file
/// @author  Boris Mikic
/// @version 2.0
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides an interface for XAL external components.

#ifndef XAL_EXTERNAL_COMPONENT_H
#define XAL_EXTERNAL_COMPONENT_H

#include "xalExport.h"

namespace xal
{
	class xalExport ExternalComponent
	{
	public:
		ExternalComponent() { }
		virtual ~ExternalComponent() { }

	protected:
		void _lock();
		void _unlock();

	};

}
#endif
