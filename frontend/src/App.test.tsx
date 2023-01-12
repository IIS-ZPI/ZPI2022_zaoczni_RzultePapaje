import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<div>a</div>);
  const linkElement = screen.getByText(/a/i);
  expect(linkElement).toBeInTheDocument();
});
