<SEO {title} />

<section>
	<Heading bind:offsetWidth>{title}</Heading>
	<FeaturedSkills {offsetWidth} />
</section>

<style>
	section {
		position: relative;
	}

	@screen <md {
		section {
			display: grid;
			gap: 1rem;
		}
	}
</style>

<script lang="ts">
	import SEO from '$lib/SEO.svelte'
	import Heading from '$lib/home/Heading.svelte'
	import FeaturedSkills from '$lib/home/FeaturedSkills.svelte'

	let offsetWidth: number

	let title = 'Ryo Fujimura'
</script>
