<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Player extends Model
{
    protected $fillable = ['team_id', 'name', 'tag'];

    public function team(): BelongsTo
    {
        return $this->belongsTo(Team::class);
    }

    public function performances(): HasMany
    {
        return $this->hasMany(Performance::class);
    }
}
