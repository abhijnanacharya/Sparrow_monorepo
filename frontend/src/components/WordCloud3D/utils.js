export function placeOnSphere(idx, total, radius = 6) {
  const k = idx + 0.5;

  const phi = Math.acos(1 - (2 * k) / total);
  const theta = Math.PI * (1 + Math.sqrt(5)) * k;

  const x = radius * Math.cos(theta) * Math.sin(phi);
  const y = radius * Math.sin(theta) * Math.sin(phi);
  const z = radius * Math.cos(phi);

  return [x, y, z];
}
