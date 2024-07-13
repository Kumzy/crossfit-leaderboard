<script setup lang="ts">
defineProps({
  auth: {
    user: String,
  },
})
//defineProps({ auth: Object })
import QRCodeCard from "@/components/QRCodeCard.vue"
const workouts = [1, 2, 3, 4, 5] // Example workout placeholders
const competitors = [
  {
    name: "John Doe",
    rank: 1,
    points: 100,
    scores: [20, 18, 22, 25, 15],
  },
  {
    name: "Jane Smith",
    rank: 2,
    points: 90,
    scores: [18, 20, 19, 20, 13],
  },
  // Add more competitors as needed
]
</script>

<template>
  <div class="container mx-auto p-4">
    <QRCodeCard
      qrCodeSrc="https://example.com/qrcode.png"
      link="https://example.com"
    />
    <h1 class="text-2xl font-bold mb-4">CrossFit Competition Leaderboard</h1>
    {{ auth.user }}
    <div class="overflow-x-auto">
      <table class="min-w-full bg-white border border-gray-200">
        <thead>
          <tr class="bg-gray-100 border-b">
            <th class="px-4 py-2">Competitor</th>
            <th class="px-4 py-2">Rank</th>
            <th class="px-4 py-2">Points</th>
            <th v-for="(workout, index) in workouts" :key="index" class="px-4 py-2">Workout {{ index + 1 }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(competitor, index) in competitors" :key="index" class="border-b hover:bg-gray-50">
            <td class="px-4 py-2">{{ competitor.name }}</td>
            <td class="px-4 py-2">{{ competitor.rank }}</td>
            <td class="px-4 py-2">{{ competitor.points }}</td>
            <td v-for="(score, i) in competitor.scores" :key="i" class="px-4 py-2">{{ score }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>

</style>
