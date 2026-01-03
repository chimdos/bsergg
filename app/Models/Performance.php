<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Performance extends Model
{
    protected $fillable = [
        'game_id', 'player_id', 'brawler_name', 'kills', 'deaths', 
        'damage_dealt', 'damage_received', 'healing', 'damage_to_safe', 
        'rating_bser', 'is_win'
    ];

    public function player(): BelongsTo
    {
        return $this->belongsTo(Player::class);
    }

    public function game(): BelongsTo
    {
        return $this->belongsTo(Game::class);
    }
}