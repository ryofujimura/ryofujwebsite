<div class="root">
	<Sidebar/>

	<div>
		<Tabs/>
		<main>
			<slot></slot>
		</main>
	</div>
</div>

<style>
	.root {
		display: grid;
	}

	@screen md {
		.root {
			grid-template-columns: 10rem 1fr;
			height: 100vh;
		}
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
