#ifndef RGSS_RENDER_QUEUE_H
#define RGSS_RENDER_QUEUE_H

#include <hltypes/harray.h>

#include "rgssExport.h"

namespace rgss
{
	class Renderable;

	/// @brief Represents a render queue to organize renderable objects by Z order and allow the functionality of RGSS's Viewport class.
	class rgssExport RenderQueue
	{
	public:
		/// @brief Destructor.
		~RenderQueue();

		/// @brief Draws this RenderQueue.
		void draw();
		/// @brief Adds a new renderable object.
		/// @param[in] renderable The renderable object to be added.
		void add(Renderable* renderable);
		/// @brief Removes the renderable object.
		/// @param[in] renderable The renderable object to be removed.
		void remove(Renderable* renderable);
		/// @brief Updates a renderable object because of a change in the Z coordinate.
		/// @param[in] renderable The renderable object that has changed.
		void update(Renderable* renderable);

	protected:
		/// @brief Contains all renderable objects;
		harray<Renderable*> renderables;

	};

}
#endif
