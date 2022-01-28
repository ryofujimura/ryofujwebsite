<div class="root">
	<Sidebar/>
	<Tabs/>
	<main>
		<slot></slot>
	</main>
</div>

<style>
	.root {
		display: grid;
		grid-template-areas: 'sidebar' 'tabs' 'main';
	}

	@screen md {
		.root {
			grid-template-areas:
				'sidebar tabs'
				'sidebar main';
			grid-template-columns: 10rem 1fr;
			grid-template-rows: auto 1fr;
			height: 100vh;
		}
	}

	main {
		grid-area: main;
		padding: 2rem;
		overflow-x: auto;
	}
</style>

<script lang="ts">
	import Sidebar from '$lib/sidebar/Sidebar.svelte'
	import Tabs from '$lib/tab/Tabs.svelte'
	import { paths } from '$lib/routes'
	import { afterNavigate } from '$app/navigation'
	import { tabs, localStore } from '$lib/store'
	import { page } from '$app/stores'
	import '../app.css'

	afterNavigate(() => {
		// add tab if user navigates to a route
		if (!$tabs.includes($page.url.pathname)) {
			$tabs.push($page.url.pathname)
		}

		// validate routes
		tabs.update(t => t.filter(tab => paths.includes(tab)))

		localStore('tabs', $tabs)
	})
</script>
