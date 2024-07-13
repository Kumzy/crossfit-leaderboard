<script setup lang="ts">
import { Link } from "@inertiajs/vue3"
import { useForm } from "@inertiajs/vue3"
import { route } from "litestar-vite-plugin/inertia-helpers"

defineProps({ errors: Object })

const form = useForm({
  name: null,
  dateStart: null,
  dateEnd: null,
  description: null,
})
</script>

<template>
  <div class="max-w-3xl mx-auto bg-white p-6 rounded-lg shadow-lg">
    <h2 class="text-2xl font-bold mb-4">Create a new competition</h2>
    <form @submit.prevent="form.post(route('competitions:create'))">
        <div class="mb-4">
            <label for="title" class="block text-sm font-medium text-gray-700">Competition name</label>
            <input type="text" id="title" v-model="form.name" name="title" placeholder="Add a competition name"
                class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
        </div>
        <div class="mb-4">
            <label for="reminder" class="block text-sm font-medium text-gray-700">Timezone</label>
            <div class="flex space-x-2 mt-1">
                <select id="reminder" name="reminder"
                    class="mt-1 block w-full px-3 py-2 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                    <option>Notification</option>
                    <option>Email</option>
                </select>
            </div>
          </div>
        <div class="mb-4">
            <label for="date" class="block text-sm font-medium text-gray-700">Competition date</label>
            <div class="flex space-x-2 items-center">
                <input type="date" id="date-start" v-model="form.dateStart" name="date-start"
                    class="mt-1 block w-1/2 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                to
                <input type="date" id="date-end" v-model="form.dateEnd" name="date-end"
                    class="mt-1 block w-1/2 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
            </div>
        </div>
        <div class="mb-4">
              <label for="date" class="block text-sm font-medium text-gray-700">Registration date</label>
              <div class="flex space-x-2 items-center">
                  <input type="date" id="date-start" v-model="form.dateStart" name="date-start"
                      class="mt-1 block w-1/2 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                  to
                  <input type="date" id="date-end" v-model="form.dateEnd" name="date-end"
                      class="mt-1 block w-1/2 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
              </div>
        </div>
        <div class="mb-4">
            <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
            <textarea id="description" name="description" v-model="form.description" rows="4" placeholder="Write a description here"
                class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md"></textarea>
        </div>
        <div class="mb-4">
              <label for="location" class="block text-sm font-medium text-gray-700">Location</label>
           <div class="grid grid-cols-2 gap-6">
                <div>
                    <label for="country" class="block text-sm font-medium text-gray-700">Country</label>
                    <select id="country" name="country" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                        <option>United States</option>
                        <!-- Add more countries as needed -->
                    </select>
                </div>
                <div>
                    <label for="city" class="block text-sm font-medium text-gray-700">City</label>
                    <input type="text" name="city" id="city" placeholder="City" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                </div>
                <div>
                    <label for="address" class="block text-sm font-medium text-gray-700">Address</label>
                    <input type="text" name="address" id="address" placeholder="Your Location" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                </div>
                <div>
                    <label for="zip" class="block text-sm font-medium text-gray-700">ZIP</label>
                    <input type="text" name="zip" id="zip" placeholder="Your Location" class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                </div>


            </div>
<!--              <div class="flex space-x-2 items-center">-->
<!--                <input type="text" id="title" v-model="form.name" name="title" placeholder="Add a competition name"-->
<!--                  class="mt-1 block w-1/2 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">-->
<!--              </div>-->
        </div>
        <div class="flex justify-end">
            <button type="submit"
                class="w-full md:w-auto flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                Create new competition
            </button>
        </div>
    </form>
</div>
</template>

<style scoped>

</style>
