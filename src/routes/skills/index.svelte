<SEO {title} />

<h1>{title}</h1>

{#each skills as skill}
	<Skill {skill} />
{/each}

<script lang="ts">
	import SEO from '$lib/SEO.svelte'
	import skills from './skills'
	import Skill from '$lib/skill/Skill.svelte'

	let title = 'Skills'
</script>
