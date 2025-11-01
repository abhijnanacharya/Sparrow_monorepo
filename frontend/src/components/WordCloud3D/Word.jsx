import React from "react";
import { Text, Float } from "@react-three/drei";
import { placeOnSphere } from "./utils";

export function Word({ word, weight, idx, total }) {
  // Get the 3D position from utils
  const pos = placeOnSphere(idx, total, 6);

  const size = 0.4 + weight * 1.0;
  const color = `hsl(${Math.floor(220 + 120 * (1 - weight))} 80% ${
    50 + Math.floor(20 * weight)
  }%)`;

  return (
    <Float speed={1 + weight} rotationIntensity={1.2} floatIntensity={1.2}>
      <Text
        position={pos}
        fontSize={size}
        color={color}
        anchorX="center"
        anchorY="middle"
        outlineWidth={0.01}
        outlineColor="black"
      >
        {word}
      </Text>
    </Float>
  );
}
