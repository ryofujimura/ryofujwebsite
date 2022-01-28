<SEO {title} />

<h1 class="h1">{title}</h1>

<section>
	{#each skills as skill}
		<Skill {skill} />
	{/each}
</section>

<script lang="ts">
	import SEO from '$lib/SEO.svelte'
	import { skills } from '../../lib/skills'
	import Skill from '$lib/skill/Skill.svelte'

	let title = 'Skills'
</script>
