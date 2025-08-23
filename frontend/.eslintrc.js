// .eslintrc.js (flat config style)
import js from "@eslint/js";
import vue from "eslint-plugin-vue";
import nuxt from "eslint-plugin-nuxt";
import tseslint from "typescript-eslint";

export default [
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    files: ["**/*.ts", "**/*.vue"],
    languageOptions: {
      parserOptions: {
        ecmaVersion: "latest",
        sourceType: "module",
      },
    },
    plugins: {
      vue,
      nuxt,
    },
    rules: {
      // Example rules
      "vue/multi-word-component-names": "off",
    },
  },
];
