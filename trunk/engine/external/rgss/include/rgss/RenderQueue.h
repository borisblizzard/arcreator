#ifndef RGSS_RENDER_QUEUE_H
#define RGSS_RENDER_QUEUE_H

#include <hltypes/harray.h>

#include "rgssExport.h"

namespace rgss
{
	class Collection;
	class Renderable;
	class Tilemap;

	/// @brief Represents a render queue to organize renderable objects by Z order and creation order and make functionality of RGSS's Viewport class easier to implement.
	class rgssExport RenderQueue
	{
	public:
		/// @brief Constructor.
		RenderQueue();
		/// @brief Destructor.
		~RenderQueue();

		/// @brief Updates this RenderQueue.
		void update();
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
		void reorder(Renderable* renderable);

	protected:
		/// @brief Contains all renderable objects.
		harray<Renderable*> renderables;
		/// @brief Contains all collection objects.
		harray<Renderable*> collections;
		/// @brief Contains all renderable objects that should be added at the next render.
		harray<Renderable*> addedRenderables;
		/// @brief Contains all collection objects that should be added at the next render.
		harray<Renderable*> addedCollections;
		/// @brief Contains all renderable objects that should be removed at the next render.
		harray<Renderable*> removedRenderables;
		/// @brief Contains all collection objects that should be removed at the next render.
		harray<Renderable*> removedCollections;
		/// @brief Needs-Sorting flag.
		bool needsSorting;

		/// @brief Updates renderables.
		void _updateRenderables();
		/// @brief Updates collections.
		void _updateCollections();

	};

}
#endif
