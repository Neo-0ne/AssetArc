<?php
/*
Template Name: Education Page
*/
get_header(); ?>

<main class="p-8 text-white max-w-6xl mx-auto">
  <h1 class="text-4xl font-bold mb-6">Learn the Smart Way</h1>
  <p class="mb-8 text-lg">Explore deep-dive articles, structuring strategies, and implementation guides.</p>

  <?php
  $args = array('category_name' => 'education', 'posts_per_page' => 6);
  $education_query = new WP_Query($args);

  if ($education_query->have_posts()) :
    echo '<div class="grid md:grid-cols-2 gap-6">';
    while ($education_query->have_posts()) : $education_query->the_post(); ?>
      <div class="bg-gray-800 p-6 rounded shadow">
        <h2 class="text-2xl font-semibold text-gold"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
        <p class="mt-2"><?php the_excerpt(); ?></p>
      </div>
    <?php endwhile;
    echo '</div>';
  else :
    echo '<p>No articles found.</p>';
  endif;

  wp_reset_postdata();
  ?>
</main>

<?php get_footer(); ?>
