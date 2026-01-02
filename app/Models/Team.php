<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Team extends Model
{
    protected $fillable = ['name', 'slug', 'region'];

    public function players(): hasMany
    {
        return $this->hasMany(Player::class);
    }
}
