<?php
// upload-review-handler.php

// Exit if accessed directly
if (!defined('ABSPATH')) {
  exit;
}

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['review_file'])) {
  // Verify the nonce
  if (!isset($_POST['_wpnonce']) || !wp_verify_nonce($_POST['_wpnonce'], 'upload_review_nonce')) {
    assetarc_display_message('Invalid nonce.', 'error');
    return;
  }

  $uploaded = $_FILES['review_file'];
  $allowed_types = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
  $max_size = 5 * 1024 * 1024; // 5MB

  if (!in_array($uploaded['type'], $allowed_types)) {
    assetarc_display_message('Invalid file type. Only PDF and DOCX files are allowed.', 'error');
  } elseif ($uploaded['size'] > $max_size) {
    assetarc_display_message('File is too large. Maximum size is 5MB.', 'error');
  } else {
    $upload_dir = wp_upload_dir()['basedir'] . '/review-uploads/';
    wp_mkdir_p($upload_dir);
    $target = $upload_dir . basename($uploaded['name']);

    if (move_uploaded_file($uploaded['tmp_name'], $target)) {
      assetarc_display_message('Upload successful: ' . esc_html($uploaded['name']));
    } else {
      assetarc_display_message('Upload failed.', 'error');
    }
  }
}
?>
