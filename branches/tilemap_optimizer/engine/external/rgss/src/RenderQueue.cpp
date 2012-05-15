#include <hltypes/harray.h>

#include "CodeSnippets.h"
#include "Renderable.h"
#include "RenderQueue.h"
#include "rgss.h"

namespace rgss
{
	RenderQueue::RenderQueue() : needsSorting(false)
	{
	}

	RenderQueue::~RenderQueue()
	{
		harray<Renderable*> renderables = this->collections + this->addedCollections + this->renderables + this->addedRenderables;
		foreach (Renderable*, it, renderables)
		{
			(*it)->dispose();
		}
	}

	bool compareFunction(Renderable* a, Renderable* b)
	{
		return (a->getZ() < b->getZ() || a->getZ() == b->getZ() && a->getCounterId() < b->getCounterId());
	}

	void RenderQueue::draw()
	{
		if (this->addedCollections.size() > 0)
		{
			this->collections += this->addedCollections;
			this->addedCollections.clear();
		}
		if (this->removedCollections.size() > 0)
		{
			this->collections -= this->removedCollections;
			this->removedCollections.clear();
		}
		foreach (Renderable*, it, this->collections)
		{
			(*it)->update();
		}
		if (this->addedRenderables.size() > 0)
		{
			this->renderables += this->addedRenderables;
			this->addedRenderables.clear();
			this->needsSorting = true;
		}
		if (this->removedRenderables.size() > 0)
		{
			this->renderables -= this->removedRenderables;
			this->removedRenderables.clear();
		}
		if (this->needsSorting)
		{
			this->renderables.sort(&compareFunction);
			this->needsSorting = false;
		}
		foreach (Renderable*, it, this->renderables)
		{
			(*it)->draw();
		}
	}

	void RenderQueue::add(Renderable* renderable)
	{
		// this part here is actually a dirty hack to separate tilemaps from normal renderable
		// objects, but it makes the high level code simpler and a lot more consistent
		if (renderable->getType() == Renderable::TYPE_TILEMAP)
		{
			this->addedCollections += renderable;
			return;
		}
		// adding the renderable into the queue
		this->addedRenderables += renderable;
	}

	void RenderQueue::remove(Renderable* renderable)
	{
		// this part here is actually a dirty hack to separate tilemaps from normal renderable
		// objects, but it makes the high level code simpler and a lot more consistent
		if (renderable->getType() == Renderable::TYPE_TILEMAP)
		{
			this->removedCollections += renderable;
			return;
		}
		// removing the renderable from the queue
		this->removedRenderables += renderable;
	}

	void RenderQueue::update(Renderable* renderable)
	{
		this->needsSorting = true;
	}

}
