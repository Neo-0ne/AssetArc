<?php
/*
Template Name: Vault Page
*/
get_header(); ?>

<main class="p-8 text-white max-w-4xl mx-auto">
  <h1 class="text-4xl font-bold mb-4">Client Vault</h1>
  <p class="mb-6">Securely access your documents and packages.</p>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    <div class="bg-gray-800 p-6 rounded">
      <h2 class="text-2xl text-gold mb-2">IBC Package</h2>
      <p class="mb-4">Your complete International Business Company formation documents.</p>
      <a href="/vault/downloads/ibc-package.pdf" class="underline text-gold">Download IBC Package</a>
    </div>

    <div class="bg-gray-800 p-6 rounded">
      <h2 class="text-2xl text-gold mb-2">Tax Summary</h2>
      <p class="mb-4">A summary of your tax obligations and filing status.</p>
      <a href="/vault/downloads/tax-summary.pdf" class="underline text-gold">Download Tax Summary</a>
    </div>
  </div>
</main>

<?php get_footer(); ?>
