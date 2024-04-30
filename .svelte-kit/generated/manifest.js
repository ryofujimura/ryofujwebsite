const c = [
	() => import("../../src/routes/__layout.svelte"),
	() => import("../../src/routes/__error.svelte"),
	() => import("../../src/routes/index.svelte"),
	() => import("../../src/routes/contact/index.svelte"),
	() => import("../../src/routes/contact/success.svelte"),
	() => import("../../src/routes/skills/index.svelte"),
	() => import("../../src/routes/about.svelte"),
	() => import("../../src/routes/works/index.svelte"),
	() => import("../../src/routes/works/[id].svelte")
];

const d = decodeURIComponent;

export const routes = [
	// src/routes/index.svelte
	[/^\/$/, [c[0], c[2]], [c[1]]],

	// src/routes/contact/index.svelte
	[/^\/contact\/?$/, [c[0], c[3]], [c[1]]],

	// src/routes/contact/success.svelte
	[/^\/contact\/success\/?$/, [c[0], c[4]], [c[1]]],

	// src/routes/skills/index.svelte
	[/^\/skills\/?$/, [c[0], c[5]], [c[1]]],

	// src/routes/about.svelte
	[/^\/about\/?$/, [c[0], c[6]], [c[1]]],

	// src/routes/works/index.svelte
	[/^\/works\/?$/, [c[0], c[7]], [c[1]]],

	// src/routes/works/[id].svelte
	[/^\/works\/([^/]+?)\/?$/, [c[0], c[8]], [c[1]], (m) => ({ id: d(m[1])})]
];

// we import the root layout/error components eagerly, so that
// connectivity errors after initialisation don't nuke the app
export const fallback = [c[0](), c[1]()];