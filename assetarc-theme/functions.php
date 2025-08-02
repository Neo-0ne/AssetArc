<?php
// Theme Setup
function assetarc_theme_setup() {
  // Add support for featured images
  add_theme_support('post-thumbnails');

  // Register nav menu
  register_nav_menus(array(
    'primary' => __('Primary Menu', 'assetarc'),
  ));

  // Add support for custom logo
  add_theme_support('custom-logo', array(
    'height' => 60,
    'flex-height' => true,
    'flex-width' => true,
  ));
}
add_action('after_setup_theme', 'assetarc_theme_setup');

// Enqueue styles and scripts
function assetarc_enqueue_assets() {
  wp_enqueue_style('assetarc-style', get_stylesheet_uri());
  wp_enqueue_script('assetarc-scripts', get_template_directory_uri() . '/assets/main.js', array('jquery'), false, true);
}
add_action('wp_enqueue_scripts', 'assetarc_enqueue_assets');

// Load security functions
require get_template_directory() . '/inc/functions-security.php';

// Load Customizer settings
require get_template_directory() . '/inc/customizer.php';

// Load newsletter handler logic
require get_template_directory() . '/inc/newsletter-handler.php';

// Load contact form handler logic
require get_template_directory() . '/inc/contact-handler.php';

// Load upload review handler logic
require get_template_directory() . '/inc/upload-review-handler.php';

// Load token request handler logic
require get_template_directory() . '/inc/token-request-handler.php';

// Load any optional review routing logic
require get_template_directory() . '/parts/review-flag-router.php';

// Display styled messages
function assetarc_display_message($message, $type = 'success') {
  $class = $type === 'success' ? 'text-green-400' : 'text-red-400';
  echo "<p class='$class mt-4'>$message</p>";
}
