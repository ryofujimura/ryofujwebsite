<SEO />

<section>
	<h1>Ryo Fujimura — 💻 Software Developer</h1>

	<div>
		{#each featuredSkills as skill}
			<article>
				<details>
					<summary>{skill.name}</summary>

					<ul>
						{#each skill.works as work}
							<li>{work.title}</li>
						{/each}
					</ul>
				</details>
			</article>
		{/each}
	</div>
</section>

<style>
	section {
		display: flex;
		flex-wrap: wrap;
		gap: 1rem;
	}
</style>

<script>
	import SEO from '$lib/SEO.svelte'
	import { skillsWithWorks } from '$lib/skills'

	let featuredSkills = skillsWithWorks
		.filter(({ featured, works }) => featured && works.length > 0)
</script>
