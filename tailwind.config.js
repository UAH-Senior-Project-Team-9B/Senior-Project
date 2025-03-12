/** @type {import('tailwindcss').Config} */

import daisyui from "daisyui";
import motion from "tailwindcss-motion";

export default {
    purge: ["./ophthalmology_portal/Core/templates/*.html"],
    theme: {
        extend: {},
    },
    plugins: [daisyui, motion],
};
