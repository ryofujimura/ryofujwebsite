<SEO {title} />

<h1 class="h1">{title}</h1>

<div class="content">
	<section class="desc">
		<p>
			Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus id aspernatur odit fugit cumque. Similique consequatur, maiores nesciunt quibusdam illum dignissimos inventore quisquam dolorem minima reprehenderit saepe repellat quis maxime.
			Similique, a odio! Aspernatur, culpa odit? Nobis delectus placeat provident minima, doloremque officiis ullam autem, repellendus in fugit ex, distinctio nemo? Mollitia ducimus numquam libero alias dolores tempora vero laboriosam?
		</p>
		<p>
			Lorem ipsum dolor sit, amet consectetur adipisicing elit. Natus quasi aliquid eligendi. Reiciendis, accusantium animi. Voluptas neque voluptatum laudantium ea maiores eligendi tempora veritatis minus quam veniam, aliquid perferendis atque.
			Magni illo quas recusandae pariatur reiciendis quia dolorum quae quod accusantium perspiciatis sequi quasi temporibus veniam fugit nisi, sint fugiat omnis quos quaerat itaque fuga. A perferendis iusto fuga dignissimos!
			Magnam in, accusantium officia harum iure neque ipsa aut ducimus voluptatibus voluptatem modi dolor ullam, facilis eligendi eaque recusandae rem asperiores ut quasi saepe incidunt placeat? Nulla aperiam voluptatem magnam!
		</p>
	</section>

	<section class="skills">
		{#each skills as skill}
			<Skill {skill} />
		{/each}
	</section>
</div>

<style>
	.content {
		display: grid;
		grid-template-areas: 'skills' 'desc';
		gap: 2rem;
	}

	.desc {
		grid-area: desc;
		line-height: 1.7;
	}

	.desc * + * {
		margin-top: 0.5em;
	}

	.skills {
		grid-area: skills;
	}

	@screen lg {
		.content {
			grid-template-columns: repeat(2, 1fr);
			grid-template-areas: 'desc skills';
		}

		.desc {
			padding: 1rem;
			@apply bg-gray-100;
		}
	}
</style>

<script lang="ts">
	import SEO from '$lib/SEO.svelte'
	import { skills } from '../../lib/skills'
	import Skill from '$lib/skill/Skill.svelte'

	let title = 'Skills'
</script>
