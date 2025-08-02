<?php
// contact-handler.php

// Exit if accessed directly
if (!defined('ABSPATH')) {
  exit;
}

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['name']) && isset($_POST['email']) && isset($_POST['message'])) {
  // Verify the nonce
  if (!isset($_POST['_wpnonce']) || !wp_verify_nonce($_POST['_wpnonce'], 'contact_form_nonce')) {
    assetarc_display_message('Invalid nonce.', 'error');
    return;
  }

  // Sanitize the input
  $name = sanitize_text_field($_POST['name']);
  $email = sanitize_email($_POST['email']);
  $message = sanitize_textarea_field($_POST['message']);

  // Validate the input
  if (!is_email($email)) {
    assetarc_display_message('Invalid email address.', 'error');
    return;
  }

  // Send the email
  $to = get_option('admin_email');
  $subject = 'New message from ' . $name;
  $body = "Name: $name\nEmail: $email\n\nMessage:\n$message";
  $headers = 'From: ' . $name . ' <' . $email . '>';

  if (wp_mail($to, $subject, $body, $headers)) {
    assetarc_display_message('Your message has been sent successfully!');
  } else {
    assetarc_display_message('There was an error sending your message. Please try again later.', 'error');
  }
}
?>
