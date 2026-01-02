<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class BrawlMatchSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $teamCR = \App\Models\Team::firstOrCreate(['slug' => 'cr'], ['name' => 'Crazy Raccoon', 'region' => 'East Asia']);
        $teamHMB = \App\Models\Team::firstOrCreate(['slug' => 'hmb'], ['name' => 'HMBLE', 'region' => 'EMEA']);

        $playersCR = [
            ['name' => 'Tensai', 'tag' => '#TENSAI1'],
            ['name' => 'Moya', 'tag' => '#MOYA1'],
            ['name' => 'Milkreo', 'tag' => '#MILKREO1'],
        ];

        foreach ($playersCR as $p) {
            $teamCR->players()->firstOrCreate(['tag' => $p['tag']], ['name' => $p['name']]);
        }

        $playersHMB = [
            ['name' => 'Lukii', 'tag' => '#LUKII1'],
            ['name' => 'Symantec', 'tag' => '#SYMANTEC1'],
            ['name' => 'BosS', 'tag' => '#BOSS1'],
        ];

        foreach ($playersHMB as $p) {
            $teamHMB->players()->firstOrCreate(['tag' => $p['tag']], ['name' => $p['name']]);
        }

        $match = \App\Models\BrawlMatch::create([
            'tournament_name' => 'World Finals 2025',
            'team_a_id' => $teamCR->id,
            'team_b_id' => $teamHMB->id,
            'score_a' => 2,
            'score_b' => 1,
            'played_at' => now(),
        ]);

        $game = $match->games()->create([
            'map_name' => 'Kaboom Canyon',
            'mode' => 'Heist',
            'game_order' => 1,
            'winner_team_id' => $teamCR->id,
        ]);

        $tensai = \App\Models\Player::where('name', 'Tensai')->first();
        $game->performances()->create([
            'player_id' => $tensai->id,
            'brawler_name' => 'Juju',
            'kills' => 13,
            'deaths' => 4,
            'damage_dealt' => 254000,
            'damage_received' => 120000,
            'damage_to_safe' => 86340,
            'rating_bser' => 1.35,
            'is_win' => true,
        ]);

        $this->command->info('Database successfully populated!');
    }
}
