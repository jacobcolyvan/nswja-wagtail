const plugin = require('tailwindcss/plugin');

module.exports = {
    content: ['./templates/**/*.html'],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Roboto', 'sans-serif'],
                'roboto-light': ['Roboto Light', 'sans-serif'],
                'roboto-medium': ['Roboto Medium', 'sans-serif'],
                'roboto-bold': ['Roboto Bold', 'sans-serif'],
            },
            fontSize: {
                banner: ['48px', { lineHeight: '112%' }],
                h1: ['32px', { lineHeight: '125%' }],
                h2: ['24px', { lineHeight: '133%' }],
                h3: ['20px', { lineHeight: '140%' }],
                h4: ['18px', { lineHeight: '145%' }],
            },
        },
    },
    plugins: [
        require('daisyui'),
        require('@tailwindcss/typography'),
        plugin(function ({ addComponents }) {
            addComponents({
                '.typography-banner': {
                    '@apply text-banner font-bold': {},
                },
                '.typography-h1': {
                    '@apply text-h1 font-bold': {},
                },
                '.typography-h2': {
                    '@apply text-h2 font-bold': {},
                },
                '.typography-h3': {
                    '@apply text-h3 font-bold': {},
                },
                '.typography-h4': {
                    '@apply text-h4 italic': {},
                },
                '.content-w': {
                    '@apply max-w-5xl mx-auto': {},
                    '@apply px-4 sm:px-6 lg:px-8': {},
                },
            });
        }),
    ],
    daisyui: {
        themes: [
            {
                jockeys: {
                    primary: '#3E95D5', // lochmare
                    secondary: '#3E3E93', // minsk
                    accent: '#8B6EBD', // amethyst
                    neutral: '#263645', // Light blue variant
                    // neutral: '#323232', // mine-shaft
                    'base-100': '#FFFFFF', // white
                    'base-200': '#F4F4F4', // wild-sand
                    'base-300': '#C6C6C6', // french-gray
                    info: '#65CFB5', // downy
                    success: '#65CFB5', // you can reuse downy or pick another color
                    warning: '#A5A5A5', // quick-silver
                    error: '#505050', // emperor
                },
            },
            'light', // keeping light theme as fallback
        ],
        darkTheme: 'jockeys', // set your theme as the default
    },
};
