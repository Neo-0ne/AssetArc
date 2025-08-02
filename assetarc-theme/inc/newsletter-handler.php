<?php
// newsletter-handler.php

// Exit if accessed directly
if (!defined('ABSPATH')) {
  exit;
}

// Check if POST request and nonce are set
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['newsletter_email'])) {
  $email = sanitize_email($_POST['newsletter_email']);

  if (!is_email($email)) {
    wp_send_json_error(['message' => 'Invalid email address.']);
    exit;
  }

  // OPTIONAL: Connect to external newsletter service or Flask endpoint
  $endpoint = 'https://your-flask-api.com/subscribe'; // Flask handler or Mailchimp proxy
  $response = wp_remote_post($endpoint, [
    'method' => 'POST',
    'timeout' => 10,
    'headers' => [
      'Content-Type' => 'application/json',
    ],
    'body' => json_encode(['email' => $email]),
  ]);

  if (is_wp_error($response)) {
    wp_send_json_error(['message' => 'Subscription failed.']);
  } else {
    wp_send_json_success(['message' => 'You are now subscribed.']);
  }
  exit;
}
?>
