<?php
/**
 * Template Name: Pricing
 */

get_header();
?>

<main class="pricing-page bg-black text-white py-16 px-6 lg:px-24">
    <div class="max-w-screen-xl mx-auto">
        <h1 class="text-4xl lg:text-5xl font-semibold mb-10 text-gold">Pricing & Access</h1>

        <p class="text-lg mb-10 max-w-3xl">
            Whether you’re a private client looking to structure your legacy or a licensed advisor scaling your impact, AssetArc offers flexible pricing tailored to your role.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 text-white">

            <!-- Private Clients -->
            <div class="bg-gray-900 rounded-2xl p-6 shadow-lg">
                <h2 class="text-2xl font-bold text-gold mb-4">Private Clients</h2>
                <p class="mb-6">
                    Explore our structuring suite and only pay when you're ready to generate documents or consult with a human advisor.
                </p>
                <ul class="space-y-2 mb-6 list-disc list-inside text-gray-300">
                    <li>Free exploration of structuring bots</li>
                    <li>Pay-per-document (pricing varies by jurisdiction)</li>
                    <li>Optional one-on-one consultations</li>
                    <li>Secure client vault with document access</li>
                </ul>
                <a href="/consultation" class="inline-block bg-gold text-black font-semibold px-6 py-3 rounded-full hover:bg-yellow-400 transition">
                    Begin Your Journey
                </a>
            </div>

            <!-- Advisor Subscriptions -->
            <div class="bg-gray-900 rounded-2xl p-6 shadow-lg">
                <h2 class="text-2xl font-bold text-gold mb-4">Advisors & Firms</h2>
                <p class="mb-6">
                    Scale your practice with automation, tokenised access for clients, and your own white-labeled version of AssetArc.
                </p>
                <ul class="space-y-2 mb-6 list-disc list-inside text-gray-300">
                    <li>Monthly or annual subscription tiers</li>
                    <li>Token packs for document generation</li>
                    <li>White-label branding and dashboard</li>
                    <li>Secure client intake and compliance tools</li>
                </ul>
                <a href="/advisor" class="inline-block bg-gold text-black font-semibold px-6 py-3 rounded-full hover:bg-yellow-400 transition">
                    Join as an Advisor
                </a>
            </div>
        </div>

        <div class="mt-16 max-w-4xl mx-auto text-center">
            <h3 class="text-2xl font-bold text-white mb-4">Need a Custom Setup?</h3>
            <p class="mb-6 text-gray-400">
                We work with high-net-worth individuals, family offices, and specialist firms on bespoke structuring and legacy projects.
            </p>
            <a href="/contact" class="inline-block border border-gold text-gold px-6 py-3 rounded-full hover:bg-gold hover:text-black transition">
                Contact Our Team
            </a>
        </div>
    </div>
</main>

<?php
get_footer();
?>
