<h1 class="text-3xl font-bold" bind:offsetWidth>
	<slot></slot>
</h1>

<style>
	h1 {
		display: inline-block;
	}

	@screen md {
		h1 {
			position: absolute;
			left: 0;
			top: 0;
		}
	}
</style>

<script lang="ts">
	export let offsetWidth: number
</script>
