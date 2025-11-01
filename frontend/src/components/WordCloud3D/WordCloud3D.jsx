import React from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { Word } from "./Word";
import { useWordCloudData } from "./hooks";

const containerStyle = {
  height: "75vh",
  width: "100%",
  background: "#0b1020",
  borderRadius: 12,
};

const cameraProps = {
  position: [0, 0, 14],
  fov: 55,
};

export default function WordCloud3D({ topics, limit }) {
  // Get the processed data from our clean, separate hook
  const processedTopics = useWordCloudData(topics, limit);

  return (
    <div style={containerStyle}>
      <Canvas camera={cameraProps}>
        <ambientLight intensity={0.8} />
        <directionalLight position={[5, 5, 5]} intensity={1.2} />

        {processedTopics.map((topic) => (
          <Word key={`${topic.word}-${topic.idx}`} {...topic} />
        ))}

        <OrbitControls enablePan={false} />
      </Canvas>
    </div>
  );
}
