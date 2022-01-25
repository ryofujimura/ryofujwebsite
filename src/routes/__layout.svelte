<div class="root">
	<Toolbar/>
	<Explorer/>

	<main>
		<slot></slot>
	</main>
</div>

<style>
	.root {
		display: grid;
	}

	@screen md {
		.root {
			grid-template-columns: 4rem 16rem 1fr;
			height: 100vh;
		}
	}

	@screen <md {
		.root {
			grid-template-rows: repeat(3, auto);
		}
	}
</style>

<script>
	import Toolbar from '$lib/Toolbar.svelte'
	import Explorer from '$lib/Explorer.svelte'
	import '../app.css'
</script>
