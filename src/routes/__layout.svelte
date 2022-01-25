<div class="root">
	<Toolbar/>

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

<script>
	import Toolbar from '$lib/Toolbar.svelte'
	import Tabs from '$lib/Tabs.svelte'
	import '../app.css'
</script>
