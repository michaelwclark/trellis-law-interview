export const timeout = seconds =>
  new Promise(resolve => setTimeout(resolve, seconds * 1000))
