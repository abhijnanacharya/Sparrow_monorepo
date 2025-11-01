import { useMemo } from "react";

export function useWordCloudData(topics, limit) {
  const safeTopics = useMemo(() => {
    return Array.isArray(topics) ? topics.slice(0, limit) : [];
  }, [topics, limit]);

  const processedTopics = useMemo(() => {
    const total = safeTopics.length || 1;
    return safeTopics.map((topic, i) => ({
      ...topic,
      idx: i,
      total: total,
    }));
  }, [safeTopics]);

  return processedTopics;
}
