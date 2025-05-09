# DataPulse Frontend

This is the frontend application for the DataPulse project, built with React, TypeScript, and Vite.

## Setup

1. Install dependencies:
   ```bash
   pnpm install
   ```

2. Run the development server:
   ```bash
   pnpm dev
   ```

3. Build for production:
   ```bash
   pnpm build
   ```

## Project Structure

- `src/`: Source code
  - `assets/`: Static assets
  - `components/`: Reusable components
  - `hooks/`: Custom React hooks
  - `pages/`: Application pages
  - `services/`: API services
  - `types/`: TypeScript type definitions
  - `utils/`: Utility functions

## Development

- Format code: `pnpm prettier --write .`
- Lint code: `pnpm lint`

## ESLint Configuration

This project uses ESLint with TypeScript support. The configuration can be expanded to enable type-aware lint rules:

```js
export default tseslint.config({
  extends: [
    ...tseslint.configs.recommendedTypeChecked,
    ...tseslint.configs.stylisticTypeChecked,
  ],
  languageOptions: {
    parserOptions: {
      project: ['./tsconfig.node.json', './tsconfig.app.json'],
      tsconfigRootDir: import.meta.dirname,
    },
  },
})
```
