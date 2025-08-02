<?php
// token-request-handler.php

// Exit if accessed directly
if (!defined('ABSPATH')) {
  exit;
}

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['name']) && isset($_POST['email']) && isset($_POST['reason'])) {
  // Verify the nonce
  if (!isset($_POST['_wpnonce']) || !wp_verify_nonce($_POST['_wpnonce'], 'token_request_nonce')) {
    assetarc_display_message('Invalid nonce.', 'error');
    return;
  }

  $name = sanitize_text_field($_POST['name']);
  $email = sanitize_email($_POST['email']);
  $reason = sanitize_textarea_field($_POST['reason']);

  if (!is_email($email)) {
    assetarc_display_message('Invalid email address.', 'error');
  } else {
    $to = get_option('admin_email');
    $subject = 'New Token Request from ' . $name;
    $body = "Name: $name\nEmail: $email\n\nReason for access:\n$reason";
    $headers = 'From: ' . $name . ' <' . $email . '>';

    if (wp_mail($to, $subject, $body, $headers)) {
      assetarc_display_message('Your token request has been submitted successfully.');
    } else {
      assetarc_display_message('There was an error submitting your request. Please try again later.', 'error');
    }
  }
}
?>
