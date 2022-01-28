<a class="link" href={route.path} on:click={() => onClick(route.path)}>
	<slot>
		{route.title}
	</slot>
</a>

<style>
	a {
		display: block;
	}
</style>

<script lang="ts">
	import { tabs, localStore } from '$lib/store'

	export let route: Route

	function onClick(path: Path) {
		if (!$tabs.includes(path)) {
			$tabs.push(path)

			localStore('tabs', $tabs)
		}
	}
</script>
